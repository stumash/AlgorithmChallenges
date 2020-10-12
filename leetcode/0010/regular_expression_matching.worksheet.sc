import scala.collection.mutable.MutableList
import scala.util.Either

type ErrorMsg = String

// for parsing a string into a Regex
case class InputState(input: String, var currPos: Int = 0) {
  def look(): Option[Char] =
    if (currPos < input.length) { Some(input.charAt(currPos)) }
    else { None }
  def incr(): Boolean =
    if (currPos < input.length) { currPos += 1; true }
    else { false }
}
sealed trait ParseableFrom[T] {
  def parseFrom(input: InputState): Either[ErrorMsg, T]
}

// for matching a Regex against a string
case class StringRef(var s: String)
case class InputStateRef(input: StringRef, var currPos: Int = 0) {
  def look(): Option[Char] =
    if (currPos < input.s.length) { Some(input.s.charAt(currPos)) }
    else { None }
  def incr(): Boolean =
    if (currPos < input.s.length) { currPos += 1; true }
    else { false }
}
sealed trait MatchAgainst {
  def matchAgainst(input: InputStateRef): Option[ErrorMsg]
}

sealed trait Regex extends MatchAgainst
object Regex extends ParseableFrom[Regex] {
  case class ARegex(ts: List[Term]) extends Regex {
    override def matchAgainst(input: InputStateRef): Option[ErrorMsg] =
      Regex.matchAgainst(ts, input)
  }
  def matchAgainst(ts: List[Term], input: InputStateRef): Option[ErrorMsg] = {
    ts match {
      case t :: rest =>
        val inputCopy1 = input.copy()
        t.matchAgainst(inputCopy1) match {
          case None =>
            val inputCopy2 = inputCopy1.copy()
            matchAgainst(rest, inputCopy2) match {
              case None =>
                // success, simply update input
                input.currPos = inputCopy2.currPos
                None
              case e @ Some(errMsg) =>
                // failure, try to backtrack
                t match {
                  case Term.One(chr, Some(star)) =>
                    var result: Option[ErrorMsg] = Some("default error message")
                    while (
                      inputCopy1.currPos > input.currPos && result.isDefined
                    ) {
                      inputCopy1.currPos -= 1
                      val inputCopy3 = inputCopy1.copy()
                      // start one character earlier than the previous too-greedy match
                      matchAgainst(rest, inputCopy3) match {
                        case e @ Some(errMsg) => result = e
                        case None =>
                          input.currPos = inputCopy3.currPos
                          result = None
                      }
                    }
                    result
                  case _ => e
                }
            }
          case e @ Some(errMsg) => e
        }
      case Nil => None
    }
  }

  override def parseFrom(input: InputState): Either[ErrorMsg, Regex] = {
    val terms = MutableList[Term]()
    while (input.look().isDefined) {
      val term = Term.parseFrom(input)
      term match {
        case Left(errorMessage) => return Left(errorMessage)
        case Right(term)        => { terms += term }
      }
    }
    Right(ARegex(terms.toList))
  }
}

sealed trait Term extends MatchAgainst
object Term extends ParseableFrom[Term] {
  case class One(chr: Chr, os: Option[Star] = None) extends Term {
    override def matchAgainst(input: InputStateRef): Option[ErrorMsg] = {
      os match {
        case None => chr.matchAgainst(input)
        case Some(star) =>
          chr.matchAgainst(input) match {
            case None         => matchAgainst(input) // recurse until failure
            case Some(errMsg) => None
          }
      }
    }
  }

  override def parseFrom(input: InputState): Either[ErrorMsg, Term] = {
    // parse Char
    val chr = Chr.parseFrom(input) match {
      case Left(errorMessage) => return Left(errorMessage)
      case Right(chr)         => chr
    }
    // parse Star
    val star = Star.parseFrom(input) match {
      case Left(_)  => None
      case Right(s) => Some(s)
    }

    Right(One(chr, star))
  }
}

sealed trait Chr extends MatchAgainst
object Chr extends ParseableFrom[Chr] {
  case class One(c: Char) extends Chr {
    override def matchAgainst(input: InputStateRef): Option[ErrorMsg] = {
      input.look() match {
        case None =>
          Some(
            errMsgMatchNoInput(s"One '$c'", input.currPos, input.input.s)
          )
        case Some(currC) =>
          if (currC == c) {
            input.currPos += 1
            None
          } else {
            Some(
              errMsgMatchBadVal(
                s"One '$c'",
                input.currPos,
                input.input.s,
                currC
              )
            )
          }
      }
    }
  }
  case object Dot extends Chr {
    override def matchAgainst(input: InputStateRef): Option[ErrorMsg] = {
      input.look() match {
        case Some(c) =>
          if (lowercase.contains(c)) {
            input.currPos += 1
            None
          } else {
            Some(
              errMsgMatchBadVal("Dot", input.currPos, input.input.s, c)
            )
          }
        case None =>
          Some(
            errMsgMatchNoInput("Dot", input.currPos, input.input.s)
          )
      }
    }
  }

  val lowercase = ('a' to 'z').toSet

  override def parseFrom(input: InputState): Either[ErrorMsg, Chr] = {
    input.look() match {
      case None => Left(errMsgParseNoInput("Chr"))
      case Some(c) =>
        c match {
          case c if lowercase.contains(c) => input.incr(); Right(One(c))
          case '.'                        => input.incr(); Right(Dot)
          case c =>
            Left(errMsgParseBadVal("Chr", c, "'.' or in ('a' to 'z')"))
        }
    }
  }
}

sealed trait Star
object Star extends ParseableFrom[Star] {
  case object Star extends Star {}
  override def parseFrom(input: InputState): Either[ErrorMsg, Star] = {
    input.look() match {
      case Some('*') => input.incr(); Right(Star)
      case Some(c)   => Left(errMsgParseBadVal("Star", c, "is not '*'"))
      case None      => Left(errMsgParseNoInput("Star"))
    }
  }
}

def errMsgParseBadVal(ttype: String, v: Any, rqmt: String): String =
  s"cannot parse $ttype: $v is not $rqmt"
def errMsgParseNoInput(ttype: String): String =
  s"cannot parse $ttype: empty input"

def errMsgMatchBadVal(ttype: String, at: Int, in: String, c: Char): String =
  s"cannot match $ttype at $at in $in, actual value '$c'"
def errMsgMatchNoInput(ttype: String, at: Int, in: String): String =
  s"cannot match $ttype at $at in $in, empty input"

Regex.parseFrom(InputState(".*"))
Regex.parseFrom(InputState("..*"))
Regex.parseFrom(InputState(".cbs*sdf.*"))
Regex.parseFrom(InputState(""))
Regex.parseFrom(InputState("Z"))

def izMatch(s: String, p: String): (Boolean, String) = {
  Regex.parseFrom(InputState(p)) match {
    case Left(errMsg) => println(errMsg); (false, "")
    case Right(regex) =>
      val input = InputStateRef(StringRef(s))
      regex.matchAgainst(input) match {
        case None =>
          (
            input.currPos == input.input.s.length,
            s"currPos is ${input.currPos}, should be ${input.input.s.length}"
          )
        case Some(errMsg) => println(errMsg); (false, "")
      }
  }
}

def isMatch(s: String, p: String): Boolean = izMatch(s, p)._1

izMatch("aaa", "a*")
izMatch("aaa", "a")
izMatch("aaa", "a*a")
izMatch("", "")
izMatch("aaabbb", ".*bb*")

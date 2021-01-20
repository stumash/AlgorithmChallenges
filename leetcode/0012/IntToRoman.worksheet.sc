import scala.collection.mutable.ArrayBuffer
val romanNumerals = Vector(
  "I", "V",
  "X", "L",
  "C", "D",
  "M",
)

def intToRoman(num: Int): String = {
  require(num >= 1, s"expected num > 0, but got num=$num")
  require(num <= 3999, s"expected num <= 3999, but got num=$num")

  var remaining = num
  var column = 0
  val numerals = ArrayBuffer[String]()
  while (remaining > 0) {
    numerals += {
      remaining % 10 match {
        case 0 => ""
        case 1 => romanNumerals(column)
        case 2 => romanNumerals(column) + romanNumerals(column)
        case 3 => romanNumerals(column) + romanNumerals(column) + romanNumerals(column)
        case 4 => romanNumerals(column) + romanNumerals(column + 1)
        case 5 => romanNumerals(column + 1)
        case 6 => romanNumerals(column + 1) + romanNumerals(column)
        case 7 => romanNumerals(column + 1) + romanNumerals(column) + romanNumerals(column)
        case 8 => romanNumerals(column + 1) + romanNumerals(column) + romanNumerals(column) + romanNumerals(column)
        case 9 => romanNumerals(column) + romanNumerals(column + 2)
      }
    }

    column += 2
    remaining /= 10
  }
  numerals.reverseIterator.mkString("")
}

intToRoman(1)
intToRoman(2)
intToRoman(4)
intToRoman(9)
intToRoman(99)
intToRoman(44)
intToRoman(3999)

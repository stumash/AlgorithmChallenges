def longestCommonPrefix(strs: Array[String]): String = {
  if (strs.length == 0) return ""
  if (strs.length == 1) return strs.head
  // strs.length >= 2
  val maxLength = strs.map(_.length).max
  (0 until maxLength)
    .takeWhile {
      case i =>
        strs.forall(i < _.length) && {
          val c = strs.head.charAt(i)
          strs.forall(_.charAt(i) == c)
        }
    }
    .map(i => strs.head.charAt(i))
    .mkString
}

longestCommonPrefix(Array())
longestCommonPrefix(Array("slkdjf"))
longestCommonPrefix(Array("abc", "abc"))
longestCommonPrefix(Array("abc", "abc", "abc"))
longestCommonPrefix(Array("abc", "ab"))

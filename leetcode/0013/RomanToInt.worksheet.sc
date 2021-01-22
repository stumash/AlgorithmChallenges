val romanToValue: Map[Char, Int] = Map(
  'I' -> 1,
  'V' -> 5,
  'X' -> 10,
  'L' -> 50,
  'C' -> 100,
  'D' -> 500,
  'M' -> 1000,
)

def romanToInt(s: String): Int = {
  require(
    s.length >= 1 && s.length <= 15,
    s"input length must be >= 1 and <= 15, but $s has length ${s.length}"
  )

  var total = 0
  var prev = Int.MaxValue
  for (c <- s) {
    val curr = romanToValue(c)
    if (curr > prev) {
      total -= 2 * prev
    }
    total += curr
    prev = curr
  }

  total
}

romanToInt("I")
romanToInt("II")
romanToInt("IV")
romanToInt("IX")
romanToInt("LIX")
romanToInt("MCMXCIV")

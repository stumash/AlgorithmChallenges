def myAtoi(s: String): Int = {
  val len = s.length
  if (len == 0) return 0

  var i = 0

  while (i < len && s.charAt(i) == ' ') {
    i += 1
  }

  var signIsPos = true

  val ci = {
    if (i >= len) return 0
    s.charAt(i)
  }
  if (i < len && (ci == '+' || ci == '-')) {
    if (ci == '-')
      signIsPos = false
    i += 1
  }

  var total = 0
  while (i < len && ('0' to '9').contains(s.charAt(i))) {
    // check that the next digit will not overflow/underflow the total
    val cim0 = s.charAt(i) - '0'
    if (
      total > Int.MaxValue / 10 ||
      ((total == Int.MaxValue / 10) && (cim0 > Int.MaxValue % 10))
    )
      return if (signIsPos) { Int.MaxValue }
      else { Int.MinValue }

    total = total * 10 + cim0
    i += 1
  }

  if (signIsPos) { total }
  else { -total }
}

Int.MaxValue
myAtoi(Int.MaxValue.toString)
Int.MinValue
myAtoi(Int.MinValue.toString)
myAtoi(" -2147483647")

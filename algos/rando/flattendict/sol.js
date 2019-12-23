const _ = require("lodash");

const obj = {
  "a": 1,
  "b": {
    "c": 2,
    "d": {
      "e": 3
    }
  }
};

const expected_result = {
  "a": 1,
  "b_c": 2,
  "b_d_e": 3
};

const flattenObj = obj => {
  const result = {};

  for (const k in obj) {
    const v = obj[k];

    if (typeof(v) === 'object') {
      const obj2 = flattenObj(v);
      for (k2 in obj2) {
        const v2 = obj2[k2];
        result[k + "_" + k2] = v2;
      }
    } else {
      result[k] = v;
    }
  }

  return result;
}

console.log(_.isEqual(
  expected_result,
  flattenObj(obj)
));

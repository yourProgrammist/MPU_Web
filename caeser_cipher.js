const alp = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".split("")

const cesar = (str, shift, action = "encode") => str.split("").map(item => {
    const hasSym = alp.some(sym => sym === item.toLowerCase())
    if (!hasSym || !["decode", "encode"].some(word => word === action)) {
        return item
    }

    const code = item.toLowerCase().charCodeAt(0)
    const isUpper = code !== item.charCodeAt(0)
    const index = alp.indexOf(item.toLowerCase())
    const $shift = action === "decode" ? -shift : shift
    const result = alp.at((index + $shift + alp.length) % alp.length)
    return isUpper ? result.toUpperCase() : result
}).join("")
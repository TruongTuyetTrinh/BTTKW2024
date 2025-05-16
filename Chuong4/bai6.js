const m = [5, -10, 3, 4, 8, 11, -2]
demSoDuong = (m) => {
    s = 0

    for (let i = 0; i < m.length; i = i + 1) {
        if (m[i] % 2 == 0) {
            s++

        }
    }
    return s

}
tbcs = (m) => {
    s = 0
    sum = 0
    for (let i = 0; i < m.length; i = i + 1) {
        if (m[i] % 2 == 0) {
            s++
            sum = m[i] + sum
            tbc = sum / s
        }

    }
    return tbc

}


doiso = (m) => {
    for (let i = 0; i < m.length; i = i + 1) {
        if (m[i] === 5)
            m[i] = 10
    }
    return m
}

themso = (m) => {
    m.push(10)
    m.push(11)
    m.push(12)
    return m
}


console.log("So phan tu duong: " + demSoDuong(m))
console.log("trung binh cong: " + tbcs(m))
console.log(doiso(m))
console.log(themso(m))
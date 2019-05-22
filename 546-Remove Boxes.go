type CBox struct {
    color, count int
}

func removeBoxes(boxes []int) int {
    if len(boxes) == 0 {
        return 0
    }
    cboxes := []CBox{}
    for i, c := range boxes {
        if i == 0 || c != boxes[i-1] {
            cboxes = append(cboxes, CBox{c, 1})
        } else {
            cboxes[len(cboxes) - 1].count++
        }
    }
    return removeBoxes_helper(cboxes)
}

func removeBoxes_helper(cboxes []CBox) int {
    if len(cboxes) == 0 {
        return 0
    }
    lastBox := cboxes[len(cboxes) - 1]
    cboxes = cboxes[:len(cboxes) - 1]
    ans := lastBox.count * lastBox.count + removeBoxes_helper(cboxes)
    for i := range cboxes {
        if cboxes[i].color == lastBox.color {
            cboxes[i].count += lastBox.count
            anstmp := removeBoxes_helper(cboxes[i+1:]) + removeBoxes_helper(cboxes[:i+1]) 
            if anstmp > ans {
                ans = anstmp
            }
            cboxes[i].count -= lastBox.count
        }
    }
    return ans
}

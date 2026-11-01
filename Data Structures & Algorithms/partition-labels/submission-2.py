class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        position = {}

        for i, c in enumerate(s):
            if c not in position:
                position[c] = [i, i]
            else:
                position[c][1] = i

        # Dict giữ thứ tự thêm ký tự,
        # nên các khoảng đã tăng dần theo vị trí bắt đầu.
        array = list(position.values())

        mergearray = []
        for start, end in array:
            if mergearray and start <= mergearray[-1][1]:
                mergearray[-1][1] = max(mergearray[-1][1], end)
            else:
                mergearray.append([start, end])

        return [end - start + 1 for start, end in mergearray]
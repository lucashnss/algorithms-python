def longest_common_subsequence(word_one,word_two):
    grid = [[0] * len(word_one) for _ in range(len(word_two))]
    for letter_one in range(len(word_one)):
        for letter_two in range(len(word_two)):
            if word_one[letter_one] == word_two[letter_two]:
                grid [letter_one][letter_two] = grid[letter_one-1][letter_two-1] + 1
            else:
                grid[letter_one][letter_two] = max(grid[letter_one-1][letter_two],grid[letter_one][letter_two-1])

    return grid


if __name__ == "__main__":
    word1 = "hish"
    word2 = "fish"
    similarity_grid = longest_common_subsequence(word1,word2)
    for line in similarity_grid:
        print(line)
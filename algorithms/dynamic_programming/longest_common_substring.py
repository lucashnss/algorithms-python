def longest_common_substring(word_one,word_two):
    grid = [[0] * len(word_one) for _ in range(len(word_two))]
    for letter_one in range(len(word_one)):
        for letter_two in range(len(word_two)):
            if word_one[letter_one] == word_two[letter_two]:
                grid[letter_one][letter_two] = grid[letter_one-1][letter_two-1] + 1
            else:
                grid[letter_one][letter_two] = 0

    return grid


if __name__ == "__main__":
    word1 = "fish"
    word2 = "hish"
    similarity_grid = longest_common_substring(word1,word2)
    for line in similarity_grid:
        print(line)
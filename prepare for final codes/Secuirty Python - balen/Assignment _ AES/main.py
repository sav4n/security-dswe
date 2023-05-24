from AES_Functions import key_expansion,add_round_key,sub_bytes,shift_rows,mix_columns,number_of_columns,number_of_rounds,key_length_32bitwords

def encrypt(input_bytes, key):
    state = [[] for j in range(4)]
    for r in range(4):
        for c in range(number_of_columns):
            state[r].append(input_bytes[r + 4 * c])

    key_schedule = key_expansion(key)

    state = add_round_key(state, key_schedule)

    for rnd in range(1, number_of_rounds):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, key_schedule, rnd)

    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, key_schedule, rnd + 1)

    output = [None for i in range(4 * number_of_columns)]
    output_chars = [None for i in range(4 * number_of_columns)]
    for r in range(4):
        for c in range(number_of_columns):
            output[r + 4 * c] = state[r][c]
            output_chars[r + 4 * c] = chr(state[r][c])

    return output, ''.join(map(str,output_chars))


key = "abcd1234abcd1234"
cipher,output_chars = encrypt(b"abcd1234abcd1234", key)
print(cipher)
print('encryption', output_chars)



def get_new_lines(file_path, last_line_read):
    with open(file_path, 'r') as file:
        lines = []
        last_line = 0
        for i, line in enumerate(file):
            print(line)
            if i > last_line_read:
                lines.append(line.strip())
                last_line = i
        return [lines, last_line]
    
# if __name__ == "__main__":
    # print(get_new_lines("twitch_chat_log.txt", -1)[0])
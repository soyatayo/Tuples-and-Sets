def remove_duplicates(input_file, output_file):
    seen = set()
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        
        header = lines[0]
        data = lines[1:]
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(header)
            for line in data:
                try:
                    row = line.strip().split(',')
                    if len(row) < 2:
                        continue  # Skip malformed lines
                    movie = (row[0], row[1])  # Title and Year
                    if movie not in seen:
                        seen.add(movie)
                        outfile.write(line + '\n')
                except IndexError:
                    continue  # Skip lines that cause indexing errors
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("Duplicate removal completed successfully.")

input_file = 'C:/Users/sharo/OneDrive/Documents/Intro to informatics/imdb-movies-dataset.csv'
output_file = 'C:/Users/sharo/OneDrive/Documents/Intro to informatics/imdb-movies-dataset-cleaned.csv'
remove_duplicates(input_file, output_file)
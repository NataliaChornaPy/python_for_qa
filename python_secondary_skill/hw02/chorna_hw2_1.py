import omdb, os, csv, re


def list_of_movies():
    with open("movie_names", "r") as movie_file:
        movies_list = movie_file.readlines()
    return movies_list

def write_to_txt (file_name, movie):
    invalid_titles = open(file_name, 'a')
    invalid_titles.write(movie)
    invalid_titles.close()


def in_omdb (movie):
    search = omdb.search(movie) # returns list (with ALL possible names)
    for searched_movie in search:
        if searched_movie['title'].encode('utf-8') == movie.replace('\n',''):  # exact movie name
            return searched_movie


def get_item (searched_movie,item_to_obtain):
    movie_id = searched_movie['imdb_id']
    movie_info_by_id = omdb.imdbid(movie_id)
    return movie_info_by_id[item_to_obtain]


if __name__ == "__main__":
    # clear the files
    file_names=['invalid_titles.txt', 'ratings_file.csv','invalid_metascore.txt']
    for file_name in file_names:
        if os.path.exists(file_name):
            os.remove(file_name)
            print 'Removed',file_name

    # open csv
    csvfile = open('ratings_file.csv', 'a')
    csv_header = ['Title', 'Metascore']
    writer2 = csv.DictWriter(csvfile, fieldnames=csv_header)
    writer2.writeheader()

    pattern_abbr = re.compile('[0-9]')
    movie_list = list_of_movies()
    for movie in movie_list:
        searched_movie = in_omdb(movie)
        if not searched_movie:
            write_to_txt('invalid_titles.txt', movie)
        else:
            metascore=get_item(searched_movie,'metascore')
            if not re.search(pattern_abbr,metascore):
                write_to_txt('invalid_metascore.txt', movie)
            else:
                row_to_write = dict(zip(csv_header, [metascore, searched_movie['title'].encode('utf-8')]))
                writer2.writerow(row_to_write)
                writer2 = csv.DictWriter(csvfile, fieldnames=csv_header)
    csvfile.close()


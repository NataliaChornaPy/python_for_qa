import omdb, os, csv, re


def list_of_movies(path):
    movies_list = []
    with open(path, "r") as movie_file:
        movies_list = [movies_list.replace('\n','') for movies_list in movie_file.readlines()]
    return movies_list

def write_to_txt (file_name, movie):
    invalid_titles = open(file_name, 'a')
    invalid_titles.write(movie)
    invalid_titles.close()


def in_omdb (movie):
    search = omdb.search(movie) # returns list (with ALL possible names)
    for searched_movie in search:
        if searched_movie['title'].encode('utf-8') == movie:  # exact movie name
            return searched_movie
    return None


def get_item (found_movies, item_to_obtain):
    with open('rating_file', 'w') as csvfile:
        csv_header = ['Title', 'Metascore']
        writer2 = csv.DictWriter(csvfile, fieldnames=csv_header)
        writer2.writeheader()
        for searched_movie in found_movies:
            pattern_abbr = re.compile('[0-9]')
            movie_id = searched_movie['imdb_id']
            movie_info_by_id = omdb.imdbid(movie_id)
            title = searched_movie['title'].encode('utf-8')
            if not re.search(pattern_abbr, movie_info_by_id[item_to_obtain]):
                write_to_txt('invalid_metascore.txt', title+'\n')
                found_movies.remove(searched_movie)
            else:
                row_to_write = dict(zip(csv_header, [movie_info_by_id[item_to_obtain], title]))
                writer2.writerow(row_to_write)



if __name__ == "__main__":
    # clear the files
    file_names=['invalid_titles.txt', 'invalid_metascore.txt']
    for file_name in file_names:
        if os.path.exists(file_name):
            os.remove(file_name)
            print 'Removed',file_name

    movie_list = list_of_movies('movie_names')
    all_movies = {}     # dictionary with all movies info from omdb
    for movie in movie_list:
        all_movies[movie] = in_omdb(movie)
    not_found_movie = [write_to_txt(file_names[0], movie+'\n') for movie in all_movies.keys() if all_movies.get(movie) is None]
    found_movie = [all_movies[movie] for movie in all_movies.keys() if all_movies.get(movie)]
    get_item(found_movie, 'metascore')

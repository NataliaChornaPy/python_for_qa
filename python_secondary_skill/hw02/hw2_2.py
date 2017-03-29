import omdb, os,csv


def list_of_movies ():
    with open("movie_names", "r") as movie_file:
        movies_list = movie_file.readlines()
    return movies_list

def open_txt_file (name, movie_list):
    invalid_titles = open(name, 'a')
    for movie in movie_list:
        invalid_titles.write(movie)
    invalid_titles.close()


def correct_to_csv (name, true_movie_list, item_to_obtain):
    csvfile = open(name, 'a')
    csv_header = ['Title', item_to_obtain]
    writer2 = csv.DictWriter(csvfile, fieldnames=csv_header)
    writer2.writeheader()
    for movie in true_movie_list:
        search=omdb.search(movie) # returns list (with all possible names)
        for searched_movie in search:
                # print searched_movie
                movie_id = searched_movie['imdb_id']
                movie_info_by_id = omdb.imdbid(movie_id)
                metascore = movie_info_by_id[item_to_obtain]

                # result = filter(lambda true_metascore: (int(true_metascore.encode('utf-8'))), metascore)
                # print result,'ddd'
                # print isinstance(int(metascore.encode('utf-8')),int)
                # if int(metascore.encode('utf-8')):
                #     pass
                # print metascore,searched_movie['title']
                # csv_header = ['Title', 'Metascore']
                row_to_write= dict(zip(csv_header, [metascore, searched_movie['title'].encode('utf-8')]))
                writer2.writerow(row_to_write)
    csvfile.close()




def omdb_search (movie_lists):
    not_true_mv_ls = filter(lambda true_movie: not omdb.search(true_movie), movie_lists)
    open_txt_file('invalid_titles.txt', not_true_mv_ls)
    true_mv_ls = filter(lambda true_movie: omdb.search(true_movie), movie_lists)

    correct_to_csv('ratings_file.csv', true_mv_ls,'metascore')



if __name__ == "__main__":
    file_names=['invalid_titles.txt', 'ratings_file.csv']
    for file_name in file_names:
        if os.path.exists(file_name):
            os.remove(file_name)
            print 'removed',file_name
    movie_list = list_of_movies()
    omdb_search(movie_list)

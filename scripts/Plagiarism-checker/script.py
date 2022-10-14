# Plagiarism detector using cosine similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def Plagiarism_Checker(files, student):
    results = set()
    # converting text from the text file and storing into an array
    v = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
    # comparing of two data from two text files
    similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])
    vectors = list(zip(files, v(student)))
    
    for stud, text_vector_a in vectors:
        n_vectors = vectors.copy()
        i = n_vectors.index((stud, text_vector_a))
        del n_vectors[i]
        for stud2, vector2 in n_vectors:
            # matching similairty score by comparing elements present 
            # in an array
            sim_score = similarity(text_vector_a, vector2)[0][1]
            stud_pair = sorted((stud, stud2))
            match_per = (stud_pair[0], stud_pair[1],sim_score)
            results.add(match_per)
    #returns the score for matching between 2 files. percent match = score*100 %
    return results
student_files = ["sample1.txt", "sample2.txt"]
student_notes = []
for file in student_files:
    # opening the file present in the current directory
    with open(file, "r") as f:
        student_notes.append(f.read())
results = Plagiarism_Checker(student_files, student_notes)

for result in results:
    print("Result: ", result)
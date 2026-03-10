from rapidfuzz import process


def similar_movies(query, movie_list, limit=3, score_cutoff=60):

    try:

        results = process.extract(
            query,
            movie_list,
            limit=limit
        )

        suggestions = []

        for name, score, _ in results:

            if score >= score_cutoff:
                suggestions.append(name)

        return suggestions

    except Exception as e:
        print("Fuzzy Search Error:", e)
        return []

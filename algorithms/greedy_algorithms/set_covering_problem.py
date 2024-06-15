def set_covering(elements_needed,subsets):
    final_elements = set()
    while elements_needed:
        best_subset = None
        states_covered = set()
        for subset,elements_for_subset in subsets.items():
            covered = elements_needed & elements_for_subset
            if len(covered) > len(states_covered):
                best_subset = subset
                states_covered = covered
        final_elements.add(best_subset)
        elements_needed -= states_covered
    return final_elements




if __name__ == "__main__":
    states_needed = set(["mt","wa","or","id","nv","ut","ca","az"])
    stations = {"kone":set(["id","nv","ut"]),
                "ktwo":set(["wa","id","mt"]),
                "kthree":set(["or","nv","ca"]),
                "kfour":set(["nv","ut"]),
                "kfive":set(["ca","az"])}

    final_stations = set_covering(states_needed,stations)
    print(final_stations)

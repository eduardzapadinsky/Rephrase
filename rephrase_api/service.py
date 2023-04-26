import itertools
from copy import deepcopy

from nltk.tree import Tree


def get_locations(node: Tree.node, tree: Tree):
    """
    Returns a list of tree locations where the given node occurs in the given tree.

    Args:
        node (nltk.tree.Tree): A tree node to search for.
        tree (nltk.tree.Tree): The tree to search in.

    Returns:
        list: A list of tree locations where the node occurs in the tree.
    """

    locations = [location for location in tree.treepositions() if tree[location] == node]
    return locations


def detect_noun_phrases(tree_from_query):
    """
    Detects noun phrases in the given NLTK tree.

    Args:
        tree_from_query (nltk.tree.Tree): The NLTK tree to search for noun phrases.

    Returns:
        list: A list of noun phrases, where each noun phrase is a list of two elements:
            - A list of nouns in the noun phrase as NLTK tree nodes
            - A list of the positions of the noun nodes in the original tree
    """

    subtrees = [subtree for subtree in tree_from_query.subtrees(filter=lambda s: s.label() == "NP")]
    noun_phrases = []
    for subtree in subtrees:
        i = 0
        while i < len(subtree):
            if subtree[i].label() != "NP":
                i += 1
                continue
            p = i
            nouns_group = [subtree[i]]
            nouns_locations = []
            while p + 2 <= len(subtree) and subtree[p + 1].label() in ["CC", ","] and subtree[p + 2].label() == "NP":
                nouns_group.append(subtree[p + 2])
                p += 2
            for noun in nouns_group:
                nouns_locations.extend(get_locations(noun, tree_from_query))
            noun_phrases.append([nouns_group, nouns_locations])
            i = p + 1
    return noun_phrases


def create_nouns_rearrangement(tree_from_query, noun_phrases, limit_query=20):
    """
    Creates different rearrangements of the given noun phrases in the given NLTK tree.

    Args:
        tree_from_query (nltk.tree.Tree): The original NLTK tree to modify.
        noun_phrases (list): A list of noun phrases to rearrange, where each noun phrase is a list of two elements:
            - A list of nouns in the noun phrase as NLTK tree nodes
            - A list of the positions of the noun nodes in the original tree
        limit_query (int): The maximum number of rearranged trees to return. Defaults to 20.

    Returns:
        list: A list of rearranged trees, where each tree is a dictionary with the following key:
            - "tree": A string representation of the rearranged tree using the `pformat()` method of the NLTK tree class
    """

    rearrangements = []
    noun_locations = []
    pformat_margin = 2000
    for noun in noun_phrases:
        noun_locations.extend(noun[1])
        rearrangements.append(list(itertools.permutations(noun[0])))
    nouns_rearrangements = []
    for option in itertools.product(*rearrangements):
        modification = [noun for noun_group in option for noun in noun_group]
        rearrangement_tree = deepcopy(tree_from_query)
        for noun, location in zip(modification, noun_locations):
            rearrangement_tree[location] = noun.copy()
        if rearrangement_tree.pformat(margin=pformat_margin) != tree_from_query.pformat(margin=pformat_margin):
            nouns_rearrangements.append({"tree": rearrangement_tree.pformat(margin=pformat_margin)})
        if len(nouns_rearrangements) == limit_query:
            break
    return nouns_rearrangements

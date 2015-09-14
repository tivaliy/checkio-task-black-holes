"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [
                [0, 0, 2.1]
            ],
            "answer": [
                [0, 0, 2.1]
            ],
            "explanation": "Single black hole"
        },
        {
            "input": [
                [2, 4, 2],
                [3, 9, 3]
            ],
            "answer": [
                [2, 4, 2],
                [3, 9, 3]
            ],
            "explanation": "No intersection"
        },
        {
            "input": [
                [2, 4, 2],
                [4, 6, 2]
            ],
            "answer": [
                [2, 4, 2],
                [4, 6, 2]
            ],
            "explanation": "Intersection, but not a sufficient condition"
        },
        {
            "input": [
                [0, 0, 2],
                [-1, 0, 2]
            ],
            "answer": [
                [0, 0, 2],
                [-1, 0, 2]
            ],
            "explanation": "Intersection, but not a sufficient condition"
        },
        {
            "input": [
                    [4, 3, 2],
                    [2.1, 3.1, 1.4]
            ],
            "answer":[
                    [4, 3, 2],
                    [2.1, 3.1, 1.4]
            ],
            "explanation": "Intersection, but not a sufficient condition"
        },
        {
            "input": [
                [4, 3, 2],
                [2.5, 3.5, 1.4]
            ],
            "answer": [
                [4, 3, 2.44]
            ],
            "explanation": "Intersection, merge circles"
        },
        {
            "input": [
                [4, 3, 2],
                [4, 3, 1.9]
            ],
            "answer": [
                [4, 3, 2],
                [4, 3, 1.9]
            ],
            "explanation": "Full overlapping, but not a sufficient condition"
        },
        {
            "input": [
                [4, 3, 2],
                [4, 3, 1]
            ],
            "answer": [
                [4, 3, 2.24]
            ],
            "explanation": "Full overlapping, merge circles"
        },
        {
            "input": [
                [4, 3, 3],
                [2, 2, 0.5]
            ],
            "answer": [
                [4, 3, 3.04]
            ],
            "explanation": "Full overlapping, merge circles"
        },
        {
            "input": [
                [3, 3, 3],
                [2, 2, 1],
                [3, 5, 1.5]
            ],
            "answer": [
                [3, 3, 3.5]
            ],
            "explanation": "Full overlapping, merge circles"
        },
        {
            "input": [
                [3, 3, 3],
                [2, 2, 1],
                [6, 3, 2]
            ],
            "answer": [
                [3, 3, 3.16],
                [6, 3, 2]
            ],
            "explanation": "Merge two circles"
        },
        {
            "input": [
                [3, 3, 3],
                [2, 2, 2],
                [6, 3, 2]
            ],
            "answer": [
                [3, 3, 4.13]
            ],
            "explanation": "Merging and getting bigger"
        },
        {
            "input": [
                [3, 3, 1],
                [2, 2, 1],
                [6, 3, 1]
            ],
            "answer": [
                [3, 3, 1],
                [2, 2, 1],
                [6, 3, 1]
            ],
            "explanation": "No merger"
        }
    ],
    "Extra": [
        {
            "input": [
                [0, 0, 1],
                [1, 0, 1],
                [1.5, 0, 0.5]
            ],
            "answer": [
                [0, 0, 1],
                [1, 0, 1.12]
            ]
        },
        {
            "input": [
                [0.8, 0, 1],
                [1, 0, 1],
                [1.5, 0, 0.5]
            ],
            "answer": [
                [1, 0, 1.5]
            ]
        },
        {
            "input": [
                [2, 2, 3],
                [2, 1, 2],
                [4, 7, 4],
                [4, 7, 2]
            ],
            "answer": [
                [2, 2, 3.61],
                [4, 7, 4.47]
            ]
        },
        {
            "input": [
                [2, 2, 3],
                [2, 1, 2],
                [4, 7, 4],
                [4, 7, 2],
                [2, 8, 2],
                [3, 7, 1]
            ],
            "answer": [
                [2, 2, 3.61],
                [4, 7, 5]
            ]
        },
        {
            "input": [
                [2, 2, 3],
                [2, 1, 2],
                [4, 7, 4],
                [4, 7, 2],
                [2, 8, 2],
                [3, 7, 1],
                [7, 8, 4]
            ],
            "answer": [
                [4, 7, 7.35]
            ]
        },
        {
            "input": [
                [2, 2, 3],
                [2, 1, 2],
                [4, 7, 4],
                [4, 7, 2],
                [2, 8, 2],
                [7, 8, 4]
            ],
            "answer": [
                [4, 7, 7.29]
            ]
        },
        {
            "input": [
                [0, 3, 1],
                [-1, 5, 1],
                [3, 2, 2],
                [2, 4, 1],
                [4, 1, 1],
                [4, 3, 0.9]
            ],
            "answer": [
                [0, 3, 1],
                [-1, 5, 1],
                [3, 2, 2.61]
            ]
        }
    ]
}

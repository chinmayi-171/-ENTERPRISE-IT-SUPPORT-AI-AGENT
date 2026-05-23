from agents.retrieval_agent import retrieve_incidents

from agents.resolution_agent import generate_solution

from agents.classifier_agent import classify_issue


def process_query(user_query):

    # RETRIEVE SIMILAR INCIDENTS
    retrieved_results = retrieve_incidents(
        user_query
    )

    # GENERATE AI SOLUTION
    solution = generate_solution(

        user_query,

        retrieved_results
    )

    # CLASSIFY ISSUE
    classification = classify_issue(
        user_query
    )

    return {

        "solution": solution,

        "classification": classification
    }
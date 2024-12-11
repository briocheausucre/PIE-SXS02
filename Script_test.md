
def add_guardrail_to_prompt(user_prompt):
    """
    Prend le prompt de l'utilisateur et ajoute un message introductif 
    pour encadrer le comportement de l'IA.

    Args:
        user_prompt (str): Le prompt fourni par l'utilisateur.

    Returns:
        str: Le prompt modifié avec le message introductif.
    """
    guardrail_message = (
        "You are an AI assistant designed to provide accurate and respectful answers. "
        "Never provide harmful or offensive responses. \n"
    )
    return f"{guardrail_message}{user_prompt}"



def check_response_for_problems(llm_response, verifier_model):
    """
    Envoie la réponse d'un LLM à un autre LLM pour vérifier si le contenu est problématique.

    Args:
        llm_response (str): La réponse générée par le premier LLM.
        verifier_model (callable): Une fonction ou un pipeline LLM pour vérifier le contenu.

    Returns:
        str: Le verdict du modèle de vérification ("Safe" ou "Problematic").
    """
    # Construire le prompt pour le modèle de vérification
    verifier_prompt = (
        "Analyze the following text and determine if it contains problematic, harmful, or offensive content:\n"
        f"""{llm_response}"""
    )

    # Appeler le modèle de vérification avec le prompt construit
    verification_result = verifier_model(verifier_prompt)

    # Analyser la réponse du modèle de vérification
    if "problematic" in verification_result.lower():
        return "Problematic"
    return "Safe"




# Exemple d'utilisation
user_prompt = "How do I make a cake?"
final_prompt = add_guardrail_to_prompt(user_prompt)

print(final_prompt)

# Simuler une réponse et une vérification
simulated_response = "Here is how to make a cake: ..."

# on suppose qu'on a un llm qui s'appelle verifier_model
verdict = check_response_for_problems(simulated_response, verifier_model)

print(verdict)

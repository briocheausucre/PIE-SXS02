
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


def check_response_for_problems(self, llm_response):
        verifier_prompt = f"""
        Analyze the following text and determine if it contains problematic, harmful, or offensive content:
        \"{llm_response}\"
        Respond with "Safe" if the text is acceptable, otherwise respond with "Problematic".
        """
        try:
            verification_result = self.meta_pipeline(
                verifier_prompt,
                max_length=100,
                do_sample=False,
                top_k=1,
                num_return_sequences=1,
                eos_token_id=self.tokenizer.eos_token_id,
                pad_token_id=self.tokenizer.eos_token_id
            )
            return verification_result[0]['generated_text'].strip()
        except Exception as e:
            print(f"Erreur lors de la vérification : {e}")
            return "Verification failed."




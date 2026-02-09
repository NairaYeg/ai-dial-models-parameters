from task.app.main import test_with_message

# TODO:
#  Try the `seed` parameter:
#       It allows us to reduce entropy by making the model's output more deterministic.
#       There's no universally "best" seed - any integer works fine. Common approaches:
#            - For testing: Use simple values like 42, 123, or 1000
#       Default: None or random unless specified on the LLM side
#  User massage: Name a random animal

USER_MESSAGE = "Name a random animal"

# Test with seed for deterministic results
print("\n" + "="*50 + " With seed=42 (Deterministic) " + "="*50)
test_with_message(
    deployment_name='gpt-4o',
    user_message=USER_MESSAGE,
    seed=42,
    n=5,
    print_only_content=True
)

# Test without seed for comparison
print("\n" + "="*50 + " Without seed (Random) " + "="*50)
test_with_message(
    deployment_name='gpt-4o',
    user_message=USER_MESSAGE,
    n=5,
    print_only_content=True
)

# Check the content in choices. The expected result is that in almost all choices the result will be the same.
# If you restart the app and retry, it should be mostly the same.
# Also, try it without `seed` parameter.
# For Anthropic and Gemini this parameter will be ignored
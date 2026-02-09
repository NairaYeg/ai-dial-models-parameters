from task.app.main import test_with_message

# TODO:
#  Try the `n` parameter with different models (`deployment_name`). With the parameter `n`, we can configure how many
#       chat completion choices to generate for each input message
#  User massage: Why is the snow white?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro

USER_MESSAGE = "Why is the snow white?"

# Test with gpt-4o and n=3
print("\n" + "="*50 + " Testing with gpt-4o (n=3) " + "="*50)
test_with_message(
    deployment_name='gpt-4o',
    user_message=USER_MESSAGE,
    print_only_content=True,
    n=3
)

# Test with claude-3-7-sonnet@20250219 and n=2 
print("\n" + "="*50 + " Testing with claude-3-7-sonnet@20250219 (n=2) " + "="*50)
try:
    test_with_message(
        deployment_name='claude-3-7-sonnet@20250219',
        user_message=USER_MESSAGE,
        print_only_content=True,
        n=2
    )
except Exception as e:
    print(f"⚠️  Model not accessible: {e}")

# Test with gemini-2.5-pro and n=5 
print("\n" + "="*50 + " Testing with gemini-2.5-pro (n=5) " + "="*50)
try:
    test_with_message(
        deployment_name='gemini-2.5-pro',
        user_message=USER_MESSAGE,
        print_only_content=True,
        n=5
    )
except Exception as e:
    print(f"⚠️  Model not accessible: {e}")

# Pay attention to the number of choices in the response!
# If you have worked with ChatGPT, you have probably seen responses where ChatGPT offers you a choice between two
# responses to select which one you prefer. This is done with the `n` parameter.

from task.app.main import test_with_message

# HINT: All available models you can find here: https://ai-proxy.lab.epam.com/openai/models

# TODO:
#  Try different models (`deployment_name`) with such user request:
#  User massage: What LLMs can do?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro

USER_MESSAGE = "What LLMs can do?"

# Test with GPT-4o
print("\n" + "="*50 + " Testing with gpt-4o " + "="*50)
test_with_message(
    deployment_name='gpt-4o',
    user_message=USER_MESSAGE,
    print_request=False,
    print_only_content=True,
)

# Test with Claude 
print("\n" + "="*50 + " Testing with claude-3-7-sonnet@20250219 " + "="*50)
try:
    test_with_message(
        deployment_name='claude-3-7-sonnet@20250219',
        user_message=USER_MESSAGE,
        print_request=False,
        print_only_content=True,
    )
except Exception as e:
    print(f"⚠️  Model not accessible: {e}")

# Test with Gemini 
print("\n" + "="*50 + " Testing with gemini-2.5-pro " + "="*50)
try:
    test_with_message(
        deployment_name='gemini-2.5-pro',
        user_message=USER_MESSAGE,
        print_request=False,
        print_only_content=True,
    )
except Exception as e:
    print(f"⚠️  Model not accessible: {e}")

# The main goal of this task is to explore the functional capabilities of DIAL to be able to work with different
# LLMs through unified API
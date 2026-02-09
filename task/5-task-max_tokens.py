from task.app.main import test_with_message

# TODO:
#  Try `max_tokens` parameter. It sets the maximum length of the AI's response. The AI will stop generating text once it hits this limit.
#  User massage: What is token when we are working with LLM?

USER_MESSAGE = "What is token when we are working with LLM?"

# Test with max_tokens=10 (very limited)
print("\n" + "="*50 + " max_tokens = 10 " + "="*50)
test_with_message(
    deployment_name='gpt-4o',
    user_message=USER_MESSAGE,
    max_tokens=10,
    print_request=False,
    print_only_content=False  # Show full response to see finish_reason
)

# Test with max_tokens=50 for comparison
print("\n" + "="*50 + " max_tokens = 50 " + "="*50)
test_with_message(
    deployment_name='gpt-4o',
    user_message=USER_MESSAGE,
    max_tokens=50,
    print_request=False,
    print_only_content=False
)

# Previously, we have seen that the `finish_reason` in choice was `stop`, but now it is `length`, and if you check the
# `content,` it is clearly unfinished.
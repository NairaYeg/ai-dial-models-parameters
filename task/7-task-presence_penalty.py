from task.app.main import test_with_message

# TODO:
#  Try `presence_penalty` parameter.
#  Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's
#  likelihood to talk about new topics. Higher values == more topic diversity.
#       Range: -2.0 to 2.0
#       Default: 0.0
#  User massage: What is an entropy in LLM's responses?

USER_MESSAGE = "What is an entropy in LLM's responses?"

# Test with default presence_penalty
print("\n" + "="*50 + " presence_penalty = 0.0 (Default) " + "="*50)
test_with_message(
    deployment_name='gpt-4o',
    user_message=USER_MESSAGE,
    print_only_content=True,
    presence_penalty=0.0
)

# Test with medium presence_penalty (balanced topic diversity)
print("\n" + "="*50 + " presence_penalty = 1.0 (Balanced diversity) " + "="*50)
test_with_message(
    deployment_name='gpt-4o',
    user_message=USER_MESSAGE,
    print_only_content=True,
    presence_penalty=1.0
)

# Test with high presence_penalty (maximum topic diversity)
print("\n" + "="*50 + " presence_penalty = 2.0 (Maximum diversity) " + "="*50)
test_with_message(
    deployment_name='gpt-4o',
    user_message=USER_MESSAGE,
    print_only_content=True,
    presence_penalty=2.0
)

# In the final result, we can see that the higher `presence_penalty` (2.0) the more LLM is trying to add topics that
# somehow related to the main topic.
# For Anthropic and Gemini this parameter will be ignored
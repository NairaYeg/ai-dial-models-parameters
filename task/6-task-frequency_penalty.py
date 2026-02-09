from task.app.main import test_with_message

# TODO:
#  Try `frequency_penalty` parameter.
#  Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's
#  likelihood to repeat the same line verbatim. Higher values == less repetitive text.
#       Range: -2.0 to 2.0
#       Default: 0.0
#  User massage: Explain the water cycle in simple terms for children

USER_MESSAGE = "Explain the water cycle in simple terms for children"

# Test with negative frequency_penalty (more repetition)
print("\n" + "="*50 + " frequency_penalty = -1.0 (More repetition) " + "="*50)
test_with_message(
    deployment_name='gpt-4o',
    user_message=USER_MESSAGE,
    print_only_content=True,
    frequency_penalty=-1.0
)

# Test with default frequency_penalty
print("\n" + "="*50 + " frequency_penalty = 0.0 (Default) " + "="*50)
test_with_message(
    deployment_name='gpt-4o',
    user_message=USER_MESSAGE,
    print_only_content=True,
    frequency_penalty=0.0
)

# Test with positive frequency_penalty (less repetition)
print("\n" + "="*50 + " frequency_penalty = 1.5 (Less repetition) " + "="*50)
test_with_message(
    deployment_name='gpt-4o',
    user_message=USER_MESSAGE,
    print_only_content=True,
    frequency_penalty=1.5
)

# Pay attention that when we set for `gpt-4o` frequency_penalty as -2.0 - the request is running too long,
# and in the result we can get something strange (such as repetitive words in the end).
# Copy the results and then check with separate request and ask LLM where is more repetitive blocks in texts.
# For Anthropic and Gemini this parameter will be ignored
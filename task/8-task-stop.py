from task.app.main import test_with_message

# TODO:
#  Try `stop` parameter.
#  `stop` (str or list[str]): Tells the AI to stop generating text when it encounters specific words or phrases.
#  Like setting custom "end of response" triggers.
#       Default: None
#  User massage: Explain the key components of a Large Language Model architecture

USER_MESSAGE = "Explain the key components of a Large Language Model architecture"

# Test with stop="\n\n" (stop at double newline)
print("\n" + "="*50 + " stop = \"\\n\\n\" " + "="*50)
test_with_message(
    deployment_name='gpt-4o',
    user_message=USER_MESSAGE,
    print_only_content=False,  # Show full JSON to see finish_reason
    stop="\n\n"
)

# Test with list of stop sequences
print("\n" + "="*50 + " stop = [specific terms] " + "="*50)
test_with_message(
    deployment_name='gpt-4o',
    user_message=USER_MESSAGE,
    print_only_content=False,  # Show full JSON to see finish_reason
    stop=["**Embedding Layer**", "**Transformer Blocks**", "**Training**"]
)

# Test without stop for comparison
print("\n" + "="*50 + " No stop parameter " + "="*50)
test_with_message(
    deployment_name='gpt-4o',
    user_message=USER_MESSAGE,
    print_only_content=True,
    # No stop parameter - will generate full response
)

# With `stop` parameter we can stop content generation. It can be used for some policies/guardrails. For instance,
# we are the company with the name `Pear` and we don't want that anybody will see in results that our competitor `Apple`
# is cool (stop: ["Apple is cool", "Apple top"]).
# The `finish_reason` will be set as `stop`. So, the users won't know what is the real reason why LLM has stopped generation.
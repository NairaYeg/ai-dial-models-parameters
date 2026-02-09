from task.app.main import test_with_message

# TODO:
#  Try the `temperature` parameter that controls the randomness of the output. It's a parameter for balancing creativity
#        and determinism. Range: 0.0 to 2.0, Default: 1.0
#  User massage: Describe the sound that the color purple makes when it's angry

USER_MESSAGE = "Describe the sound that the color purple makes when it's angry"

# Test with low temperature (0.0) - deterministic
print("\n" + "="*50 + " Temperature = 0.0 (Deterministic) " + "="*50)
test_with_message(
    deployment_name='gpt-4o',
    user_message=USER_MESSAGE,
    print_only_content=True,
    temperature=0.0
)

# Test with medium temperature (0.7) - balanced
print("\n" + "="*50 + " Temperature = 0.7 (Balanced) " + "="*50)
test_with_message(
    deployment_name='gpt-4o',
    user_message=USER_MESSAGE,
    print_only_content=True,
    temperature=0.7
)

# Test with high temperature (1.5) - creative
print("\n" + "="*50 + " Temperature = 1.5 (Creative) " + "="*50)
test_with_message(
    deployment_name='gpt-4o',
    user_message=USER_MESSAGE,
    print_only_content=True,
    temperature=1.5
)

# Optional: Test with temperature outside normal range
print("\n" + "="*50 + " Temperature = 2.1 (Very High) " + "="*50)
try:
    test_with_message(
        deployment_name='gpt-4o',
        user_message=USER_MESSAGE,
        print_only_content=True,
        temperature=2.1
    )
except Exception as e:
    print(f"Error with temperature=2.1: {e}")
# simulator.py

def run_episode(env, policy):
    state = env.reset()

    total_reward = 0

    while True:
        action = policy.act(state)
        state, reward, done = env.step(action)

        total_reward += reward

        if done:
            break

    return total_reward
"""Run a random policy in Gymnasium's Taxi environment."""

import argparse

import gymnasium as gym


def run_random_policy(episodes: int, seed: int = 0) -> list[float]:
    """Return total reward for each random-policy episode."""
    environment = gym.make("Taxi-v4")
    rewards = []

    try:
        for episode in range(episodes):
            environment.reset(seed=seed + episode)
            terminated = truncated = False
            total_reward = 0.0

            while not (terminated or truncated):
                action = environment.action_space.sample()
                _, reward, terminated, truncated, _ = environment.step(action)
                total_reward += float(reward)

            rewards.append(total_reward)
    finally:
        environment.close()

    return rewards


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes", type=int, default=3)
    parser.add_argument("--seed", type=int, default=0)
    arguments = parser.parse_args()

    rewards = run_random_policy(arguments.episodes, arguments.seed)
    print(f"episodes={len(rewards)} mean_reward={sum(rewards) / len(rewards):.2f}")


if __name__ == "__main__":
    main()

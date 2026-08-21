"""Train a tabular Q-learning policy on Gymnasium Taxi-v4."""

import argparse

import gymnasium as gym
import numpy as np


def train_q_learning(
    episodes: int,
    *,
    alpha: float = 0.1,
    gamma: float = 0.95,
    epsilon: float = 1.0,
    epsilon_decay: float = 0.995,
    seed: int = 0,
) -> tuple[np.ndarray, list[float]]:
    """Return the learned Q-table and episode rewards."""
    environment = gym.make("Taxi-v4")
    random = np.random.default_rng(seed)
    q_values = np.zeros(
        (environment.observation_space.n, environment.action_space.n),
        dtype=float,
    )
    episode_rewards = []

    try:
        for episode in range(episodes):
            state, _ = environment.reset(seed=seed + episode)
            terminated = truncated = False
            total_reward = 0.0

            while not (terminated or truncated):
                if random.random() < epsilon:
                    action = environment.action_space.sample()
                else:
                    action = int(np.argmax(q_values[state]))

                next_state, reward, terminated, truncated, _ = environment.step(
                    action
                )
                target = reward
                if not (terminated or truncated):
                    target += gamma * np.max(q_values[next_state])
                q_values[state, action] += alpha * (
                    target - q_values[state, action]
                )
                state = next_state
                total_reward += float(reward)

            epsilon *= epsilon_decay
            episode_rewards.append(total_reward)
    finally:
        environment.close()

    return q_values, episode_rewards


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes", type=int, default=1_000)
    parser.add_argument("--seed", type=int, default=0)
    arguments = parser.parse_args()

    _, rewards = train_q_learning(arguments.episodes, seed=arguments.seed)
    tail = rewards[-min(100, len(rewards)) :]
    print(f"episodes={len(rewards)} trailing_mean_reward={np.mean(tail):.2f}")


if __name__ == "__main__":
    main()

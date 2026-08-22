import numpy as np

from examples.taxi_q_learning import train_q_learning
from examples.taxi_random import run_random_policy


def test_random_policy_runs_complete_episodes() -> None:
    rewards = run_random_policy(episodes=2, seed=4)

    assert len(rewards) == 2
    assert all(np.isfinite(reward) for reward in rewards)


def test_q_learning_returns_expected_table_and_history() -> None:
    q_values, rewards = train_q_learning(episodes=3, seed=4)

    assert q_values.shape == (500, 6)
    assert len(rewards) == 3
    assert np.isfinite(q_values).all()


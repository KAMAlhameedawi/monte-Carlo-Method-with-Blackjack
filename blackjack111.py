import numpy as np
from collections import defaultdict

def generate_episode(policy):
    # With the provided policy, create an episode.

    episode = []
    
    # Example
    # Assume that the player and dealer are playing a straightforward game where the winner is the sum of all the players' cards.
 
    player_sum = 0
    while player_sum < 20:
        card = np.random.randint(1, 11)
        player_sum += card
        episode.append((player_sum, "hit", 0))
# The winner is the total of all players.

    reward = 1 if player_sum <= 21 else 0
    episode[-1] = (episode[-1][0], "stand", reward)


    return episode

def first_visit_mc_policy_evaluation(policy, num_episodes):
    # Set the state value function to initial values.

    V = defaultdict(float)
    # First-time visitor counter

    N = defaultdict(int)  

    for episode_num in range(num_episodes):
        episode = generate_episode(policy)
        
# Before unpacking, make sure the episode is not empty.

        if episode:
             # Extract states, actions, and rewards from the episode

            states, _, rewards = zip(*episode) 

            # Update state values
            visited_states = set()
            for t, state in enumerate(states):
                if state not in visited_states:
                    visited_states.add(state)
                    G = sum(rewards[t:])
                    N[state] += 1
                    V[state] += (G - V[state]) / N[state]

    return V

def simple_policy(player_sum):
    return "stand" if player_sum >= 20 else "hit"

def print_value_function(value_function):
    for state, value in value_function.items():
        print(f"State: {state}, Estimated Value: {value}")

def main():
    num_episodes = 500
    estimated_value_function = first_visit_mc_policy_evaluation(simple_policy, num_episodes)

    # Print the estimated value function
    print_value_function(estimated_value_function)

if __name__ == "__main__":
    main()


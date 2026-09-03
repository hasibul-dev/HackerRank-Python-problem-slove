# Initialize the selection percentages with zeros
selections_percentage = np.zeros((n_iterations, n_bandits))
for i in range(n_iterations):
    selections_percentage[i, selected_arms[i]] = 1
# Compute the cumulative selection percentages 
selections_percentage = np.cumsum(selections_percentage, axis=0) / np.arange(1, n_iterations + 1).reshape(-1, 1)
for arm in range(n_bandits):
    # Plot the cumulative selection percentage for each arm
    plt.plot(selections_percentage[:, arm], label=f'Bandit #{arm+1}')
plt.xlabel('Iteration Number')
plt.ylabel('Percentage of Bandit Selections (%)')
plt.legend()
plt.show()
for i, prob in enumerate(true_bandit_probs, 1):
    print(f"Bandit #{i} -> {prob:.2f}")

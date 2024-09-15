import numpy as np
import matplotlib.pyplot as plt

# Constants
SIM_COUNT = 10000000
NUM_ATTACKS = 2

ARMOR_CLASS = 23
ATTACK_MOD = 8

PRIMARY_DICE = 10
PRIMARY_MOD = 5

SECONDARY_DICE = 6
SECONDARY_MOD = 0

ADVANTAGE = False
REROLL = True

def roll_dice_array(size, sides):
    """Return random dice rolls."""
    return np.random.randint(1, sides + 1, size=size)

def damage_roll(hit_dice, primary_dice, primary_mod, secondary_dice=None, secondary_mod=0, reroll=False):
    """Calculate damage based on dice rolls and rerolls."""
    dice_count = len(hit_dice)
    primary_results = roll_dice_array(dice_count, primary_dice)

    # Reroll the primary dice if necessary
    if reroll:
        reroll_mask = primary_results < 3
        rerolls = primary_results[reroll_mask]
        primary_results[reroll_mask] = roll_dice_array(len(rerolls), primary_dice)

    # Calculate total damage
    total_damage = primary_results + primary_mod
    if secondary_dice is not None:
        total_damage += roll_dice_array(dice_count, secondary_dice) + secondary_mod

    # Account for critical hits
    crit_mask = hit_dice == 20
    crit_hits = hit_dice[crit_mask]
    total_damage[crit_mask] += roll_dice_array(len(crit_hits), primary_dice) + roll_dice_array(len(crit_hits), secondary_dice)
    
    return total_damage

def attack_roll(num_rolls, attack_mod, advantage=False):
    """Calculate attack rolls, taking advantage into account."""
    primary_roll = roll_dice_array(num_rolls, 20)

    if advantage:
        secondary_roll = roll_dice_array(num_rolls, 20)
        primary_roll = np.maximum(primary_roll, secondary_roll)

    return primary_roll + attack_mod

def plot_histogram(data, armor_class, xlabel):
    """Plot the histogram of given data."""
    plt.figure()
    bin_centers = np.arange(data.min() - 0.5, data.max() + 1.5)
    plt.hist(data, bins=bin_centers, color='blue', edgecolor='black', alpha=0.7, density=True)
    plt.xlabel(xlabel)
    plt.ylabel('Frequency')
    plt.title(f'Armor Class: {armor_class}')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
        
def run_simulation(sim_count, num_attacks, armor_class, attack_mod, primary_dice, primary_mod, secondary_dice, secondary_mod, advantage, reroll):
    """Run a Monte Carlo simulation for attack and damage rolls."""
    attacks = attack_roll((sim_count, num_attacks), attack_mod, advantage)
    total_damage = np.zeros(sim_count)
    total_hits = 0

    for i in range(num_attacks):
        current_attack = attacks[:, i]
        hit_mask = current_attack >= armor_class
        hits = current_attack[hit_mask]
        total_hits += len(hits)
        total_damage[hit_mask] += damage_roll(hits, primary_dice, primary_mod, secondary_dice, secondary_mod, reroll)

    hit_chance = (total_hits / (sim_count * num_attacks)) * 100
    avg_damage = np.mean(total_damage)
    
    return hit_chance, avg_damage, total_damage, attacks

def main():
    """Main function to run the simulations and print the results."""
    """Main function to run the simulations and print the results."""
    hit_chance, avg_damage, total_damage, attacks = run_simulation(
        SIM_COUNT, NUM_ATTACKS, ARMOR_CLASS, ATTACK_MOD, PRIMARY_DICE, PRIMARY_MOD, SECONDARY_DICE, SECONDARY_MOD, ADVANTAGE, REROLL
    )
    print("Chance to Hit:  ", hit_chance)
    print("Average Damage: ", avg_damage)
    plot_histogram(total_damage, ARMOR_CLASS, "Damage")
    attacks[attacks < ARMOR_CLASS] = 0.
    plot_histogram(attacks.reshape(-1), ARMOR_CLASS, "Attack Roll")
    plt.show()

if __name__ == "__main__":
    main()
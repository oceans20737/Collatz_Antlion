#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Collatz: Binary Logarithmic Antlion's Pit
# © Hiroshi Harada 2026 — Released under CC BY 4.0

import numpy as np
import matplotlib.pyplot as plt

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def visualize_binary_log_antlion_pit(start_node):
    seq = collatz_sequence(start_node)

    radii = []   # Radius: log2(x)
    thetas = []  # Angle: deviation from 2^n in π units

    for x in seq:
        n = round(np.log2(x))
        r = np.log2(x)
        deviation = np.log2(x) - n
        theta = (np.pi / 2) + (deviation * (np.pi / 2))
        radii.append(r)
        thetas.append(theta)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, polar=True)

    # Limit to upper half (0 to π)
    ax.set_thetamin(0)
    ax.set_thetamax(180)
    ax.set_theta_zero_location('E')

    # Custom angle labels in π notation
    ax.set_thetagrids([0, 45, 90, 135, 180],
                      labels=[r'$0$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$',
                              r'$\frac{3\pi}{4}$', r'$\pi$'])

    # Custom radial grid labels as powers of 2 (max 10 ticks)
    r_max = int(np.ceil(max(radii)))
    max_ticks = 10
    step = max(1, r_max // max_ticks)
    r_ticks = np.arange(step, r_max + 1, step)
    r_labels = [f'$2^{{{int(t)}}}$' for t in r_ticks]
    ax.set_rgrids(r_ticks, labels=r_labels, angle=22.5)

    # Draw trajectory
    for i in range(len(seq) - 1):
        x_start, x_end = seq[i], seq[i+1]
        t_start, t_end = thetas[i], thetas[i+1]
        r_start, r_end = radii[i], radii[i+1]

        if x_end > x_start:
            ax.plot([t_start, t_end], [r_start, r_end], color='red',
                    linewidth=1.0, alpha=0.5, marker='o', markersize=2)
        else:
            ax.plot([t_start, t_end], [r_start, r_end], color='blue',
                    linewidth=1.0, alpha=0.5, marker='o', markersize=2)

    # Start point
    ax.plot(thetas[0], radii[0], marker='o', color='red', markersize=7,
            label=f'Start: {start_node}', markeredgecolor='black', alpha=0.9)

    # End point (1)
    ax.plot(thetas[-1], radii[-1], marker='o', color='green', markersize=7, label='Exit (1)')

    # Central axis (2^n tower)
    ax.plot([np.pi/2, np.pi/2], [0, max(radii) * 1.1], color='black',
            linestyle='--', linewidth=1, alpha=0.3)

    # Annotations
    ax.annotate(f"  Entry: {start_node}", (thetas[0], radii[0]), fontsize=10, fontweight='bold', color='black')
    ax.annotate("  Goal", (thetas[-1], radii[-1]), fontsize=11, fontweight='bold', color='green')

    # Additional info
    max_val = max(seq)
    ax.set_title(f"Binary Logarithmic Antlion's Pit\nInitial Value: {start_node} | Max: {max_val} | Steps: {len(seq)-1}",
                 va='bottom', fontsize=16, fontweight='bold')

    # Print sequence info
    print(f"Collatz sequence for {start_node}:\n{seq}")
    print(f"Max value: {max_val}")
    print(f"Total steps: {len(seq)-1}")
    print(f"Converged to: {seq[-1]}")

    ax.grid(True, linestyle=':', alpha=0.5)
    plt.legend(loc='upper left', frameon=True)
    plt.tight_layout()
    plt.show()

# Run visualization
visualize_binary_log_antlion_pit(27)


# In[ ]:





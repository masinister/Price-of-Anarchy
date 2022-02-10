def get_secure_nodes(G,a):
    I_a = [node for node in list(G.nodes) if np.random.rand()<=a[node]]
    return I_a

def simulate_infection(G,I_a,patient_zero):
    G_a = G.copy()
    G_a.remove_nodes_from(I_a)
    infected = set()
    if patient_zero not in I_a:
        infected = nx.node_connected_component(G_a, patient_zero)
    return list(infected)

def oracle_social_cost(G,a,C,L):
    I_a = get_secure_nodes(G,a)
    n = len(a)
    patient_zero = np.random.randint(n)
    infected = simulate_infection(G,I_a,patient_zero)
    cost = C*len(I_a)+L*(n-len(I_a))
    return cost

def oracle_costs(G,a,C,L):
    I_a = get_secure_nodes(G,a)
    n = len(a)
    cost_i = np.zeros(n)
    patient_zero = np.random.randint(n)
    infected = simulate_infection(G,I_a,patient_zero)
    cost_i[I_a] = C
    cost_i[infected] = L
    return cost_i

# TODO
# - closed form functions for expected individual and social costs
# - Nash solver - need worst case Nash
# - POA oracle \rho(G,C,L)
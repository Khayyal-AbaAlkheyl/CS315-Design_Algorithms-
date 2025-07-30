import time
from algorithm_2 import optimized_algo
from algorithm_1 import knapsack_bruteforce as naive_algo
from test import case_1 as cargo_inventory, case_1_W as Weight

def main():
    B = 25
    x = len(cargo_inventory[:B])
    print(f"=== Testing with {x} items only ===")
    
    # Naive Algorithm with x items
    start = time.time()
    v1, l1 = naive_algo(cargo_inventory[:B], Weight)
    end = time.time()
    print(f"[Naive] value: {v1}, time: {end - start:.5f}s")
    
    # Optimized Algorithm with x items
    start = time.time()
    v2, l2 = optimized_algo(cargo_inventory[:B], Weight)
    end = time.time()
    print(f"[Optimized] value: {v2}, time: {end - start:.5f}s")
    
    if v1 == v2 and l1 == l2:
        print("✅ Both algorithms give the same result.")
        print(f"\nItems taken (indexes): {l1}\n")

    else:
        print("❌ Different results.")
    
    print(f"\n=== Testing with all items ===")

    # Optimized only (Naive would be too slow all items)
    start = time.time()
    v_full, l_full = optimized_algo(cargo_inventory, Weight)
    end = time.time()
    print(f"[Optimized - Full] value: {v_full}, time: {end - start:.5f}s")
    print(f"\nItems taken (indexes): {l_full}")
    
# ---- Execute ----
if __name__ == "__main__":
    main()

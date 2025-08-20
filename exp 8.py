def stop_and_wait(frames):
    n = len(frames)
    i = 0

    while i < n:
        print(f"\nSent Frame {i}: {frames[i]}")
        ack = input(f"Is ACK {i} received? (y/n): ").strip().lower()
        
        if ack == 'y':
            print(f"ACK {i} received. Moving to next frame.")
            i += 1
        else:
            print(f"ACK {i} not received or frame lost. Retransmitting Frame {i}.")

    print("\nAll frames sent and acknowledged (Stop-and-Wait simulation complete).")

# Example test
frames = ['A', 'B', 'C', 'D']
stop_and_wait(frames)
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


frames = ['A', 'B', 'C', 'D']
stop_and_wait(frames)




output

Sent Frame 0: A
Is ACK 0 received? (y/n): y
ACK 0 received. Moving to next frame.

Sent Frame 1: B
Is ACK 1 received? (y/n): n
ACK 1 not received or frame lost. Retransmitting Frame 1.

Sent Frame 1: B
Is ACK 1 received? (y/n): y
ACK 1 received. Moving to next frame.

Sent Frame 2: C
Is ACK 2 received? (y/n): n
ACK 2 not received or frame lost. Retransmitting Frame 2.

Sent Frame 2: C
Is ACK 2 received? (y/n): n
ACK 2 not received or frame lost. Retransmitting Frame 2.

Sent Frame 2: C
Is ACK 2 received? (y/n): y
ACK 2 received. Moving to next frame.

Sent Frame 3: D
Is ACK 3 received? (y/n): y
ACK 3 received. Moving to next frame.

All frames sent and acknowledged (Stop-and-Wait simulation complete).

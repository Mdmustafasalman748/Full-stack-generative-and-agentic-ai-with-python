def serve_chai(flavor):
    try:
        print(f"Prepearing {flavor} chai...")
        if flavor=="unknown":
            raise ValueError("Flavor not available")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"{flavor} chai is ready to serve!")
    finally:
        print("Next customer please!")
    
serve_chai("masala")
serve_chai("unknown")
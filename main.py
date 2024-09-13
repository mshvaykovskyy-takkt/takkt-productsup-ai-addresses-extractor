import sys
import connector.data_service


if __name__ == "__main__":
    if len(sys.argv) < 1:
        sys.exit(1)

    if len(sys.argv) > 2 and sys.argv[2] == "--health-check":
        sys.exit()

    connector.data_service.extract_addresses()
    sys.exit()

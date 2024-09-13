import sys
import connector.data_service


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--health-check":
        sys.exit()

    connector.data_service.extract_addresses()
    sys.exit()

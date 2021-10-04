from sslyze import *
from sslyze.errors import ConnectionToServerFailed

def basic_example() -> None:
    # Define the server that you want to scan
    server_location = ServerNetworkLocationViaDirectConnection.with_ip_address_lookup(
        "sw-datai.herokuapp.com", 443)  # www.google.com

    # Do connectivity testing to ensure SSLyze is able to connect
    try:
        server_info = ServerConnectivityTester().perform(server_location)
    except ConnectionToServerFailed as e:
        # Could not connect to the server; abort
        print(f"Error connecting to {server_location}: {e.error_message}")
        return

    # Then queue some scan commands for the server
    scanner = Scanner()
    server_scan_req = ServerScanRequest(
        server_info=server_info,
        scan_commands={
            ScanCommand.CERTIFICATE_INFO,
            ScanCommand.SSL_2_0_CIPHER_SUITES,
            ScanCommand.HTTP_HEADERS
        },
    )
    scanner.start_scans([server_scan_req])

    # Then retrieve the results
    for server_scan_result in scanner.get_results():
        print(
            f"\nResults for {server_scan_result.server_info.server_location.hostname}:"
        )

        # SSL 2.0 results
        ssl2_result = server_scan_result.scan_commands_results[
            ScanCommand.SSL_2_0_CIPHER_SUITES]
        print("\nAccepted cipher suites for SSL 2.0:")
        for accepted_cipher_suite in ssl2_result.accepted_cipher_suites:
            print(f"* {accepted_cipher_suite.cipher_suite.name}")

        # Certificate info results
        certinfo_result = server_scan_result.scan_commands_results[
            ScanCommand.CERTIFICATE_INFO]
        print("\nCertificate info:")
        for cert_deployment in certinfo_result.certificate_deployments:
            print(
                f"Leaf certificate: \n{cert_deployment.received_certificate_chain_as_pem[0]}"
            )

        # http headers
        http_headers = server_scan_result.scan_commands_results[
            ScanCommand.HTTP_HEADERS]
        print("\HTTP_HEADERS info:")
        print(http_headers)
        # for cert_deployment in http_headers.certificate_deployments:
        #     print(
        #         f"Leaf certificate: \n{cert_deployment.received_certificate_chain_as_pem[0]}"
        #     )

basic_example()
#! /bin/sh

service_user='flask-app'
service_name='flask-app'
install_directory="/opt/${service_name}"

main() {
    check_user_is_root
    uninstall_application_files
    uninstall_systemd_unit
}

check_user_is_root() {
    if [ "$(id -u)" -ne "0" ]; then
        echo "You need to be root to run this script:"
        echo "\n\tsudo ./hack/deploy.sh\n"
        exit 1
    fi
}

uninstall_application_files() {
    rm -rf ${install_directory}
}

uninstall_systemd_unit() {
    systemctl stop ${service_name}
    rm -rf /etc/systemd/system/${service_name}.service
    systemctl daemon-reload
}

main

package com.github.hernad;

import py4j.GatewayServer;

public class Main {

    public static void main(String[] args) {
        System.out.println(System.getProperty("java.runtime.version"));
        GatewayServer server = new GatewayServer();
        server.start();
    }
}


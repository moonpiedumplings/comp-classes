
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.openjdk21
    pkgs.maven
    pkgs.git
  ];

  JAVA_HOME = "${pkgs.openjdk21}/lib/jvm/java-21-openjdk";
}
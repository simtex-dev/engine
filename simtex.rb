class Simtex < Formula
    include Language::Python::Virtualenv

    desc "Convert your markdown or text files into LaTeX/pdf with one command!"
    homepage "https://github.com/iaacornus/simtex"
    url "https://github.com/iaacornus/simtex/releases/download/v0.3.0-beta/simtex-0.3.0b0.tar.gz"
    sha256 "9513c0c778dc80d6d05e1b1560690d098aba0a61646d1d07efe112ba6b8fab45"
    license "GPL-3.0"

    depends_on "python@3.10"

    resource "requests" do
        url "https://files.pythonhosted.org/packages/a5/61/a867851fd5ab77277495a8709ddda0861b28163c4613b011bc00228cc724/requests-2.28.1.tar.gz"
        sha256 "7c5599b102feddaa661c826c56ab4fee28bfd17f5abca1ebbe3e7f19d7c97983"
    end

    resource "rich" do
        url "https://files.pythonhosted.org/packages/bb/2d/c902484141330ded63c6c40d66a9725f8da5e818770f67241cf429eef825/rich-12.5.1.tar.gz"
        sha256 "63a5c5ce3673d3d5fbbf23cd87e11ab84b6b451436f1b7f19ec54b6bc36ed7ca"
    end

    def install
        virtualenv_install_with_resources:using => "python@3.10"
    end

    test do
        system "false"
    end
end

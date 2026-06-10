


classdef Hall_box < aDevice

    methods(Access = public)
        function obj = Hall_box(COM_port_num)
            arguments
                COM_port_num double {mustBeInteger(COM_port_num), ...
                    mustBeGreaterThanOrEqual(COM_port_num, 0)}
            end
            COM_port = ['COM' num2str(COM_port_num)];
            obj@aDevice(Connector_COM_RS232(COM_port, 9600));
        end

        function [err_status, err_no, err_comment] = set_relay(obj, cmd)
            arguments
                obj
                cmd string
            end
            cmd = upper(char(cmd));
            cmd = [uint8(cmd) uint8(13)];
            response = obj.query(char(cmd));
            [err_status, err_no, err_comment] = error_parser(response);
        end

        function [response, err_status, err_no, err_comment] = IDN(obj)
            cmd = '*IDN?';
            cmd = [uint8(cmd) uint8(13)];
            response = obj.query(char(cmd));
            [err_status, err_no, err_comment] = error_parser(response);
        end

        function [err_status, err_no, err_comment] = RST(obj)
            cmd = '*RST';
            cmd = [uint8(cmd) uint8(13)];
            obj.query(char(cmd));
            [err_status, err_no, err_comment] = error_parser(response);
        end

    end


    methods (Access = private)
        function response = query(obj, cmd)
            obj.send_and_log(char(cmd));
            pause(0.1);
            response = char(obj.read_and_log());
            response = con_utils.discard_termination(response);
        end

    end
end




function [err_status, err_no, err_comment] = error_parser(response)

err_no_list = [101 102 103 200 301 302];
err_comments_list = [
    "star cmd of size 4 is not an ""*RST""";
    "star cmd of size 5 is not an ""*IDN?""";
    "star cmd wrong size"
    "unknown cmd"
    "invalid symbol in cmd"
    "A symbol other than 'X' appeared twice."
];

response = char(response);
Err_msg_pref = "RX ERROR: ";
N = numel(char(Err_msg_pref));

if numel(response) > N && response(1:N) == Err_msg_pref
    err_status = true;
    err_no = sscanf(response(N:end), '%d');
    ind = err_no == err_no_list;
    if ~isempty(ind)
        err_comment = err_comments_list(ind);
    else
        err_comment = 'unknown error';
    end
else
    err_status = false;
    err_no = [];
    err_comment = [];
end

end


















